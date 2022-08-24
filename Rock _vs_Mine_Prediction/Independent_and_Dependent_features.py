class independent_dependent_features():

    def idv(self,data):
        x=data.iloc[:,:60]
        y=data.iloc[:,60]
        return x,y