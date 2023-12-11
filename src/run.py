from d11 import stage1, stage2
import time


if __name__ == '__main__':
    st = time.time()
    st_p = time.process_time()

    stage2.run()
    
    et = time.time()
    et_p = time.process_time()
    print(f'=====\nExecution time: {et - st} seconds\nCPU Time: {et_p - st_p}')
