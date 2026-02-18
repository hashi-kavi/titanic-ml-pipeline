import pandas as pd 



class TitanicDataPipeline:
    def __init__(self, file_path):
    
        self.df = pd.read_csv(file_path)
        print("pipeline initialized and data loaded")
        print(self.df.head())
        print(self.df.isnull().sum())
        self.df.info()

    def handle_missing_values(self):
        # 1.drop Cabin column(too many missing values)
        if 'Cabin' in self.df.columns:
         self.df= self.df.drop('Cabin', axis = 1)
        # 2. fill missing Age values with median of each Pclass
        self.df['Age'] = self.df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))

        # 3. fill Embarked with mode
        self.df['Embarked']=self.df['Embarked'].fillna(self.df['Embarked'].mode()[0])

        print("missing values handled successfully!")


    def feature_engineering(self):
      # create FamilySize
      self.df['FamilySize'] = self.df['SibSp']+self.df['Parch']+1
      
      # create IsAlone
      self.df['IsAlone'] = (self.df['FamilySize']== 1).astype(int)
      print("features engineered.")

    def finalize_features(self):
       cols_to_drop = ['Name','PassengerId','Ticket','Parch','SibSp']
       self.df.drop(columns=cols_to_drop,inplace=True)
       print(f"Droped unnecessary columns:{cols_to_drop}")

    def show_info(self):
       print("\n--CLEANED DATA INFO-- ")
       print(self.df.isnull().sum())
       self.df.info()


    def save_file(self,output_path):
       self.df.to_csv(output_path , index = False)# index = false remove the index 
       print(f"Cleaned data save to {output_path}")

    def encode_data(self):
       #one hot encoding for embarked
        self.df = pd.get_dummies(self.df,columns=['Embarked'],drop_first=True)  
        #drop_first drom one column so by other two can represent it like If Embarked_Q=0 and Embarked_S=0 → it must be C     
       #binary encoding for sex 
        self.df['Sex'] = self.df['Sex'].map({'male':0,'female':1})

# --- THE 'MAIN' BLOCK ---
if __name__ == "__main__":
   # this runs only when execute script directly
   pipeline = TitanicDataPipeline("../data/Titanic-Dataset.csv")
   pipeline.handle_missing_values()
   pipeline.feature_engineering()
   pipeline.finalize_features()
   pipeline.encode_data()
   pipeline.save_file("../data/cleaned_titanicdata.csv")
   pipeline.show_info()