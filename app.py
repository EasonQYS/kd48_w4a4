from lmdeploy.serve.gradio.turbomind_coupled import run_local
from lmdeploy.messages import TurbomindEngineConfig

import os
base_path = './model'
os.system('git lfs install')
os.system(f'git lfs clone https://code.openxlab.org.cn/yisheng/snh_pocket48_1.git {base_path}')
print('********git clone***********')
os.system(f'cd {base_path} && git lfs pull')
print('***************pull finish**********')

backend_config = TurbomindEngineConfig(max_batch_size=8)
model_path = base_path
run_local(model_path, backend_config=backend_config, server_name="openxlab")
