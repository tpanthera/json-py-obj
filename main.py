# create object
import json
data = '{}'
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
