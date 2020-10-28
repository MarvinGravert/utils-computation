import numpy as np

def fitSphere(dataX,dataY,dataZ):
    
    assert dataX is not None
    
    assert len(dataX)==len(dataY)==len(dataZ)
    A=np.vstack([dataX,dataY,dataZ,np.ones(len(dataX))]).T
    b=np.array(dataX)**2+np.array(dataY)**2+np.array(dataZ)**2
    x,residuals,*_=np.linalg.lstsq(A,-b,rcond=None)
    ##x=[targetvector,..]
    radius=np.linalg.norm(x[0:3])
    return [x[0:3],radius]
    


if __name__ == "__main__":
    x=[1,2]
    y=[2,3]
    z=[3,4]
    t=fitSphere(x,y,z)
    print(t)