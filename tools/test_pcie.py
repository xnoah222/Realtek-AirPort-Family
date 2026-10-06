from pathlib import Path
import subprocess,tempfile,os,sys
sdk=subprocess.check_output(['xcrun','--show-sdk-path'],text=True).strip()
os.environ['CPLUS_INCLUDE_PATH']=sdk+'/usr/include/c++/v1'
if len(sys.argv)<2: raise SystemExit('Usage: python3 test_pcie.py SOURCE/Feixiao [OTHER_SOURCE/Feixiao]')
for root in map(Path,sys.argv[1:]):
 s=(root/'src/compat/linux/pci.h').read_text();s=s[s.index('static inline int pci_find_capability'):s.index('static inline void *pci_ioremap_bar')]
 c='''#include <cassert>
#include <cerrno>
using u16=unsigned short;
#define PCI_CAP_ID_EXP 16
struct pci_dev{};int base=0x70,reads=0,writes=0,last=0,fail=0;u16 value=0;
int find(pci_dev*,int id){assert(id==16);return base;}
struct Ops{int(*pci_find_capability)(pci_dev*,int);}ops{find},*rtw88_pci_io_ops=&ops;
int pci_read_config_word(pci_dev*,int pos,u16*out){++reads;last=pos;*out=value;return fail;}
int pci_write_config_word(pci_dev*,int pos,u16 val){++writes;last=pos;value=val;return 0;}
'''+s+'''
int main(){pci_dev d;u16 out;
 for(int cap:{0x40,0x70,0x80,0xc0}){base=cap;value=0x1234;
 assert(!pcie_capability_read_word(&d,0x10,&out)&&out==0x1234&&last==cap+0x10);
 assert(!pcie_capability_set_word(&d,0x28,0x10)&&last==cap+0x28&&value==0x1234);
 value=0;assert(!pcie_capability_set_word(&d,0x28,0x10)&&value==0x10);
 assert(!pcie_capability_clear_word(&d,0x28,0x10)&&value==0);
 fail=-5;int old=writes;assert(pcie_capability_set_word(&d,0x28,1)==-5&&writes==old);fail=0;
 }
 for(int cap:{0,0x20,0xff}){base=cap;int old=reads;out=99;assert(pcie_capability_read_word(&d,0x10,&out)&&!out&&reads==old);}
 base=0xf0;assert(pcie_capability_set_word(&d,0x28,1));base=0x70;assert(pcie_capability_clear_word(&d,3,1));
}
'''
 c='#include <initializer_list>\n'+c
 with tempfile.TemporaryDirectory() as t:
  p=Path(t);(p/'test.cpp').write_text(c)
  subprocess.run(['xcrun','clang++','-std=c++17','-fsanitize=undefined',str(p/'test.cpp'),'-o',str(p/'test')],check=True)
  subprocess.run([str(p/'test')],check=True)
 print('PASS PCIe offsets, bounds, missing capabilities and error propagation:',root)
