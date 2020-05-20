
```{r}
library(dplyr)
library(stringr)
library(treemap)
mydata<-read.csv('NYPD_Complaint_Data_Current__Year_To_Date_xhz.csv')
ddf2<-select(mydata,Offense.Description___CrimeDescription)
ddf2<-count(group_by(ddf2, Offense.Description___CrimeDescription))
ddf2$offense <- sapply(str_split(ddf2$Offense.Description___CrimeDescription,"___"),'[',1)
ddf2$crime <- sapply(str_split(ddf2$Offense.Description___CrimeDescription,"___"),'[',2)
treemap(ddf2, index=c("offense","crime"), vSize="n", type="index", title='number of the crime' ) 

```




```{r}
library(dplyr)
library(ggplot2)
mydata$hour <- sapply(str_split(mydata$TimeOfOccurence ,":"),'[',1)
ddf3<-count(group_by(mydata, hour))
names(ddf3)<-c("hour","number")
as.numeric(as.character(ddf3$hour))
order(ddf3$hour)
ggplot(ddf3, aes(x=hour, y=number, group=1)) +geom_line()+ggtitle("x and y are continuous variables")+theme_bw()+theme_update(text = element_text(size=16))+geom_point(size=2)

```

