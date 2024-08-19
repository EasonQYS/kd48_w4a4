import os
base_path = './model'
os.system('git lfs install')
os.system(f'git clone https://code.openxlab.org.cn/yisheng/snh_pocket48_4bit.git {base_path}')
print('********git clone***********')
os.system(f'cd {base_path} && git lfs pull')
print('***************pull finish**********')

os.system(f'lmdeploy serve gradio {base_path} --server-name 0.0.0.0 --server-port 7860 --model-format awq')
