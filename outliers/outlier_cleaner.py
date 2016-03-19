#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    npoints = len(net_worths)
    max_ind = int(0.9 * npoints)
    
    for i in range(npoints):
        cleaned_data.append((ages[i][0], net_worths[i][0], abs(net_worths[i][0] - predictions[i][0])))

    cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])
    cleaned_data = cleaned_data[:max_ind]
    
    
    
    return cleaned_data

