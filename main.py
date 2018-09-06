# create object
import json
data = '{"":"325:9","agent_id":"94:1","agent_config_type_id":"302:1","agent_config_type_name":"STANDARD","system_property_config_json":{"docker_id":"137:0","sys_id":"153:0"},"job_id":"cbtj999999999999999999999","job_name":"cb_standard_dialogue_dummy_job_v1","job_type_id":"102:1","job_type_name":"STANDARD_TRAINING","job_log_dir":"/mnt/ai/shared/chatbot/models_repo/model_logs/training/94:1/cbtj999999999999999999999/","job_property_config_json":{"model_id":"103:1","model_name":"standard_dialogue_keras_model_v1","model_framework_id":"404:1","model_framework_name":"RASA","model_category_type_id":"201:2","model_category_type_name":"DIALOGUE","model_type_id":"303:3","model_type_name":"STANDARD","model_template_type_id":"406:1","model_template_type_name":"STANDARD_KERAS_POLICY","configured_model_script_file_path":"/mnt/ai/shared/chatbot/models_repo/dialogue/scripts/94:1/103:1/cbtj999999999999999999999/cbtj999999999999999999999-103:1.py","domain_config_property_json":{"domain_config_yaml_nfs_file_path":"/mnt/ai/shared/chatbot/dataset/dialogue/domain_config/94:1/202:2/resturant_dialogue_config.yaml","domain_config_yaml_s3_file_path":"https://S3/mnt/ai/shared/chatbot/dataset/dialogue/domain_config/94:1/202:2/resturant_dialogue_config.yaml"},"dataset_id":"609:1","dataset_name":"resturant_dialogue_story","dataset_type_id":"505:1","dataset_type_name":"STORIES","dataset_config_property_json":{"dataset_nfs_path":"/mnt/ai/shared/chatbot/dataset/dialogue/stories/94:1/202:2/resturant_dialogue_story.md","dataset_s3_path":"http://S3/mnt/ai/shared/chatbot/dataset/dialogue/stories/94:1/202:2/resturant_dialogue_story.md"},"batch_size":"32","epoch":"1"}}'
loadjsoon = json.loads(data)
lsitobj = []

class user:
    def __init__(self,dicttest):
        try:
            # we can change here dicttest['id'] to 'dicttest['mai-id'] later , changing name here will not change how an end user calls .
            self.id = dicttest['id']
        except KeyError:
            self.id = None
            print('blank key value ')
        try:
            self.job_property_config_json = job_property_config_json_class(dicttest['job_property_config_json'])
        except KeyError:
            self.job_property_config_json = None
        try:
            self.agent_config_type_id = dicttest['agent_config_type_id']
        except KeyError:
            self.agent_config_type_id = None
        try:
            self.agent_config_type_name = dicttest['agent_config_type_name']
        except KeyError:
            self.agent_config_type_name = None
        try:
            self.job_id = dicttest['job_id']
        except KeyError:
            self.job_id = None
        try:
            self.job_name = dicttest['job_name']
        except KeyError:
            self.job_name = None
        try:
            self.job_type_id = dicttest['job_type_id']
        except KeyError:
            self.job_type_id = None
        try:
            self.job_type_name = dicttest['job_type_name']
        except KeyError:
            self.job_type_name = None
        try:
            self.job_log_dir = dicttest['job_log_dir']
        except KeyError:
            self.job_log_dir = None



class job_property_config_json_class:
    def __init__(self,obj):
        try:
            self.mode_id = obj['mode_id']
        except KeyError:
            self.mode_id = None
        try:
            self.domain_config_property_json = domain_config_property_json_class(obj['domain_config_property_json'])
        except KeyError:
            self.domain_config_property_json = None

class domain_config_property_json_class:
    def __init__(self,obj):
        try:
            self.domain_config_yaml_nfs_file_path = obj['domain_config_yaml_nfs_file_path']
        except KeyError:
            self.domain_config_yaml_nfs_file_path = None
        try:
            self.domain_config_yaml_s3_file_path = obj['domain_config_yaml_s3_file_path']
        except KeyError:
            self.domain_config_yaml_s3_file_path = None

class system_property_config_json_class:
    def __init__(self,obj):
        try:
            self.docker_id = obj['docker_id']
        except KeyError:
            self.sys_id = None
        try:
            self.sys_id = obj['sys_id']
        except KeyError:
            self.sys_id = None



#for k in loadjsoon:

tmp = user(loadjsoon)

lsitobj.append(tmp)
print(lsitobj)








'''
algo -
parse json to python object)
class: (pass python dict object)
  # is simple dict
  try :
      store dict value 
  except KeyError:
        error handling msg
  # nested dict object
  try :
      call class of nested dict
  except:
      error handling

# create nested class
class :
    try:
      store dict value
    except:
      error handling 
  
'''
