from _decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import treepredict as tp

ls = None
ts = None


def parsing():
    data = []
    with open("agaricus-lepiota.data", 'r') as fid:
        txt = fid.readlines()
        for slot in txt:
            word = slot.split(',')
            leng = len(word[-1])
            word[-1] = word[-1][:leng-1]
            data.append(word)
    set_div = int(0.6666666667 * len(data))
    print("len(data):", len(data))
    learning_set = data[0:set_div]
    test_set = data[set_div:]
    #print("len(learningset):", len(learning_set))
    #print("len(testset):", len(test_set))
    return learning_set, test_set

def run():
    ls, ts = parsing()
    results = []
    for perc in range(1, 101):
        actualls = ls[:int(perc/100*len(ls))]
        tp.attributes = ['cap-shape','cap-surface','cap-color','bruises?','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']
        #tp.attributes = ['buying','maint','doors','persons','lug_boot','safety']
        #tp.attributes = ['AGE', 'MENOPAUSE', 'TUMOR-SIZE', 'INV-NODES', 'NODE-CAPS', 'DEG-MALIG','BREAST','BREAST-QUAD','IRRADIAT']
        #tp.attributes = ['parents','has_nurs','form','children','housing','finance','social','health']
        #tp.ReprTree(tp.buildtree(ls))
        #tp.drawtree(tp.buildtree(ls))
        fail = 0
        total = len(ts)
        tree = tp.buildtree(actualls)
        #tp.prune(tree,0.1)
        for example in ts:
            value = example[-1]
            #result = tp.mdclassify(example, tree)
            result = tp.classify(example, tree)
            if list(result.keys())[0] != value:
                fail += 1
        success = round(Decimal((total-fail)/total*100), 2)
        #print("\nFail Attempt:", fail)
        #print("Total:", total)
        #print("Success:", success, '%')
        results.append(success)

    xAxis = list(range(1, 101))
    plt.plot(xAxis, results)
    plt.axis([0, 100, 0, 100])
    plt.xlabel('Dimension of learning set')
    plt.ylabel('Success rate')
    plt.show()

    print(max(results))
    x = xAxis[results.index(max(results))]
    print(x)
    print("Error Rate:", str(100-max(results))+'%')

    tree = tp.buildtree(ls[:int(71/100*len(ls))])
    tp.drawtree(tree)
run()
