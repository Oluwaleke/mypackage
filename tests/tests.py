from mypackage import module, myModule

def test_top_n():
    """

    making sure top_n works correctly

    """
    assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], 'incorrect'
    assert myModule.top_n([5,9,8,6,4], 3) == [9,8,6], 'incorrect'
    assert myModule.top_n([10,12,24,17,14], 3) == [24,17,14], 'incorrect'
    assert myModule.top_n([80,30,20,70,40,10,60], 5) == [80,70,60,40,30], 'incorrect'
    