from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        url = super(AccountAdapter, self).get_login_redirect_url(request)
        # user = request.user
        test = request.user.first_name
        if test == '0':
            url ='education/'
        if test == '1':
            url = 'company/'
        '''
        # pseudocode, change it to actual logic
        # check user role and return a different URL
        role = get_user_role(user)
        if role == 'student':
            url = student_login_redirect_url
        if role == 'teacher':
            url = teacher_login_redirect_url
        '''
        return url