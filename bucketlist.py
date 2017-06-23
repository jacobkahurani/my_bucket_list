class user_accounts(object):
    def __init__(self,user_name,email_address,password):
        self.user_list=[]
        self.user_info={}
        #self.user_name=user=name
        #self.email_address=email_address
        #self.password=password

    def sign_up(user_name,email_address,password,re_password):
        self.user_info={user_name:user_email, password:user_name}
        if re_password==password and self.user_info not in self.user_list:
            
            self.user_list.append(self.user_info)
        else:
            return "user name already exists or passwords do not match"

    def log_in(user_name,password):
        if password and self_user_info[password] in self.user_list:
            #return bucket_list
        else:
            "user name does not exist. Sign up for free"

class bucket_list(object):
    def __init__ (self,activity,description,edit):
        #self.activity =activity
        #self.description = description
        #self.edit = edit

    def add_activity(self,activity_name):