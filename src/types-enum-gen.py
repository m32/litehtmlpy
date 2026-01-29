def gen(result, lenum, lids):
    result.append(f'    py::enum_<lh::{lenum}>(m, "{lenum}", py::arithmetic())\n')
    for lid in lids:
        result.append(f'        .value("{lid}", lh::{lenum}::{lid})\n')
    result.append('        .export_values()\n')
    result.append('    ;\n')

def main():
    fname = '../litehtml/include/litehtml/types.h'
    with open(fname, 'rt') as fp:
        lines = fp.readlines()

    ignore = ['_baseline_type', 'cbc_size_mode', 'cbc_value_type']
    result = []
    lenum = None
    lids = []
    for line in lines:
        if lenum is None:
            ll = line.strip().split()
            if ll and ll[0] == 'enum':
                if ll[1] not in ignore:
                    lenum = ll[1]
                    lids = []
        elif lenum:
            ll = line.strip()
            if not ll or ll == '{':
                continue
            if ll == '};':
                gen(result, lenum, lids)
                lenum = None
            else:
                ll = ll.split()[0].split(',')[0]
                lids.append(ll)
    result = ''.join(result)
    with open('types-enum.h', 'wt') as fp:
        fp.write(result)
main()
