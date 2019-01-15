from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def mean_squared_error(true, pred):
    return np.mean((pred - true)**2)

def root_mean_square_error(true,pred):
    return np.sqrt(mean_squared_error(true,pred))

def mean_absolute_error(true,pred):
    return np.mean(np.abs(pred - true))

def sum_squared_error(true,pred):
    return np.sum((pred - true)**2)

def r2_score(true,pred):
    y_bar = np.mean(true)
    SSE = np.sum((pred - true)**2)
    SST = np.sum((true - y_bar)**2)
    return 1.-(SSE/SST)

def adj_r2(rsquare, num_data, num_features):
    temp = (1-rsquare)*(num_data-1)
    temp = temp/(num_data-num_features-1)
    temp = 1 - temp
    return temp

def standard_error_estimate(true,pred,num_data):
    SSE = np.sum((pred - true)**2)
    return np.sqrt(SSE/(num_data-2))

def plot_model_results(X,y,ypred):
    plt.style.use('seaborn')
    plt.scatter(ypred,y,s=55)
    plt.plot([min(y),max(y)],[min(y),max(y)],'r-')
    plt.xlabel('Predicted')
    plt.ylabel('True');
    plt.show()
    
def p_vals_per_coef(pred, true, coefs, X):
    sse =  sum_squared_error(pred,true)/ float(X.shape[0] - X.shape[1])
    standard_error = np.array([np.sqrt(np.diagonal(sse * np.linalg.inv(np.dot(X.T, X))))])
    t_stats = coefs / standard_error
    p_vals = 2 * (1 - stats.t.cdf(np.abs(t_stats), true.shape[0] - X.shape[1]))
    return p_vals

def model_score(true, pred, X, verbose=0):
    r2 = r2_score(true,pred)
    adjr2 = adj_r2(r2,X.shape[0],X.shape[1])
    if verbose:
        plot_model_results(X,true,pred)
        print("Mean Squared Error: ", mean_squared_error(true,pred))
        print("Root Mean Squared Error: ", np.sqrt(mean_squared_error(true,pred)))
        print("Mean Absolute Error: ",mean_absolute_error(true,pred))
        print("R2: ", r2)
        print("Adj R2: ", adjr2)
        print("Standard Error of Estimate: ", standard_error_estimate(true,pred,X.shape[0]))
    return r2, adjr2


if __name__ == '__main__':

    from sklearn.linear_model import LinearRegression

    X = np.random.uniform(-10,10,100)
    y = X + np.random.normal(0,0.5, 100) + 9
    X = X.reshape(-1,1)

    lr = LinearRegression()
    lr.fit(X, y)
    preds = lr.predict(X)

    _ = model_score(y, preds, X, verbose = 1)
