import os

BUILD_BRANCHES = ["master"]
DEPLOY_BRANCHES = BUILD_BRANCHES

CONFIG_KEYS = {'version', 'crp_type', 'crp_config', 'flag', 'enable_flag_input'}
CRP_CONFIG_KEYS = {
    'source_image_project_id', 'source_image_family', 'ssh_username', 'ports',
    'cpu_cores', 'mem_limit_gb', 'storage_limit_gb', 'nested', 'internet_access',
}

GOOGLE_PROJECT_ID = os.environ.get('GOOGLE_PROJECT_ID')
GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
PACKER_COMPUTE_ZONE = os.environ.get('CLOUDSDK_COMPUTE_ZONE', 'europe-west1-d')

AVATAO_USER = 'user'
CONTROLLER_USER = 'controller'
CONTROLLER_FUNCTIONS_REGION = 'europe-west1'

SSHD_CONFIG = '''Port 22
AuthenticationMethods password publickey
PasswordAuthentication yes
UsePAM yes
UseDNS no
'''
