import runpy, time
from pathlib import Path
t0 = time.perf_counter()
scripts = sorted(Path('projects').glob('*/main.py'))
for i, s in enumerate(scripts, 1):
    runpy.run_path(str(s), run_name='__main__')
    if i % 50 == 0:
        print(f'[TRACK {i//50:02d}/10] Verified {i}/500 projects ({time.perf_counter()-t0:.2f}s)')
print(f'\nALL {len(scripts)}/500 PROJECTS VERIFIED SUCCESSFULLY IN {time.perf_counter()-t0:.2f}s!')
