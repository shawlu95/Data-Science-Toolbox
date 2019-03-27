library(MASS)
library(ISLR)

names(Boston)
save(Boston,file="data.Rda")
write.csv(Boston, file = "MyData.csv")
?Boston
plot(medv~lstat, data=Boston)

fit1=lm(medv~lstat, data=Boston)
fit1
summary(fit1)

abline(fit1, col='red')
names(fit1)
confint(fit1)

predict(fit1, data.frame(lstat=c(5,10,15)), interval="confidence")

# multiple
fit2=lm(medv~lstat+age, data=Boston)
summary(fit2)

# use all predictors
fit3=lm(medv~., data=Boston)
summary(fit3)
par(mfrow=c(2,2))
plot(fit3)

# remove two variables
fit4=update(fit3,~.-age-indus)
summary(fit4)

### nonlinearity
fit5=lm(medv~lstat*age, Boston)
summary(fit5)

# add quadratic term, with identity function
fit6=lm(medv~lstat+I(lstat^2), Boston)
summary(fit6)

attach(Boston)
par(mfrow=c(1,1))
plot(medv~lstat)
points(lstat, fitted(fit6), col='red', pch=20)

fit7=lm(medv~poly(lstat, 4))
points(lstat, fitted(fit7), col='blue', pch=20)

# plotting character, cex=2 doubles size
plot(1:20, 1:20, pch=1:20, cex=2)

# function
regplot=function(x, y){
  fit=lm(y~x)
  plot(x, y)
  abline(fit, col='red')
}
attach(Boston)
regplot(lstat, medv)

# allow extra arguments
regplot=function(x, y, ...){
  fit=lm(y~x)
  plot(x, y, ...)
  abline(fit, col='red')
}

regplot(lstat, medv, xlab='Price', ylab='Sales', col='blue', pch=20)

### qualitative predictor
fix(Carseats)
names(Carseats)

lm.fit=lm(Sales~.+Income:Advertising+Price:Age,data=Carseats)
summary(lm.fit)
contrasts(Carseats$shelveLoc)
