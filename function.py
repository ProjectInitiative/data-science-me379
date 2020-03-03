#!/usr/bin/env python3

def get_mae_dtr(max_leaf_nodes, x_train, y_train, x_test, y_test):
    # Define Model

    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import mean_absolute_error
    
    model_decision_tree = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)

    # Fit model
    model_decision_tree.fit(x_train, y_train)

    # Predict
    y_test_pred = model_decision_tree.predict(x_test)

    # Evaluate
    mae = mean_absolute_error(y_test, y_test_pred)

    return mae

def currency(num):
    
    import locale
    _ = locale.setlocale(locale.LC_ALL, '')
    return str(locale.currency(num, grouping=True))

def build_score_randomforest(x_train, y_train, x_test, y_test):
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_error
    # Define
    model = RandomForestRegressor(random_state=1)

    # Fit
    _ = model.fit(x_train, y_train)

    # Predict
    y_test_pred = model.predict(x_test)

    # Evaluate
    mae = mean_absolute_error(y_test, y_test_pred)
    return mae