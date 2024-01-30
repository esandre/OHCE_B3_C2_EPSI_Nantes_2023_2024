from utilities.langueStub import LangueStub


class LangueSpy(LangueStub):
    __félicitationsConsultées = False

    def félicitationsConsultées(self):
        return self.__félicitationsConsultées

    def féliciter(self):
        self.__félicitationsConsultées = True
