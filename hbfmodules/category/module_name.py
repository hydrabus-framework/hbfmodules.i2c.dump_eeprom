from hydrabus_framework.modules.AModule import AModule


class ClassName(AModule):
    def __init__(self, hbf_module):
        super(ClassName, self).__init__(hbf_module)
        self.meta.update({
            'name': '',
            'version': '',
            'description': '',
            'author': ''
        })

    def run(self):
        """
        Our code here
        :return:
        """
