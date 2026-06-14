#!/usr/bin/env python3

import litai
from litai.studio import Studio
from litai.gpu import GPUType

def run_sieve_on_gpu(gpu_type):
    studio = Studio()
    session = studio.start_session(gpu_type=gpu_type)
    session.run_script('sieve_l40s_hot_corridor.py')
    results = session.get_results()
    session.save_results(results)
    session.stop()

if __name__ == '__main__':
    run_sieve_on_gpu(GPUType.L40S)