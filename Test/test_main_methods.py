from BaraaValidator.transactionValidators import validateTransactionsFolder, validateTransactionsFile
import os
def test_mainMethods():
    dirpath = os.path.dirname(__file__)
    filepath = os.path.join(dirpath, 'transaction.json')
    assert (validateTransactionsFile(filepath)) == True
test_mainMethods()