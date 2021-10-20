import time
from Node import NodePy, NodePyExecutor

if __name__ == '__main__':
    #############################################
    # define functions locally inside main body #
    #############################################
    def hello3():
        print()
        time.sleep(1)
        print()
        print('Sending a callback.')
        return hello2


    def hello2():
        print()
        print('Callback called.')


    def hello(a=''):
        print()
        time.sleep(5)
        print('This is a delayed message.' + ' ' + a)


    node = NodePy()
    ###########################
    # Check the Native Python #
    ###########################
    # print('Starting Native Py')
    # print()
    # print()
    # output = hello3()
    # hello()
    # output()

    #########################
    # Check the Node Python #
    #########################
    print()
    print()
    print('Starting NodePy')
    print()
    print()


    def execute_func(x) -> None:
        x()


    @NodePyExecutor
    def hello4(msg):
        time.sleep(10)
        print('executed using NodePyExecutor: ', msg)


    #####
    hello4('This is a test message')

    output2 = None
    res = None
    NodePy.exec(hello, ())
    NodePy.exec(hello, ())
    NodePy.exec(hello3, ()).then(execute_func)
    NodePy.exec(hello3, ()).then(execute_func)
    NodePy.exec(hello3, ()).then(execute_func)
    NodePy.exec(hello3, ()).then(execute_func)
    NodePy.exec(hello3, ()).then(execute_func)
    NodePy.exec(hello3, ()).then(execute_func)
    NodePy.exec(hello, ())
    node.exec(hello, ())
    node.exec(hello, ())
    node.exec(hello, ())
    node.exec(hello, ())
    node.exec(hello, ())
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)
    node.exec(hello3, ()).then(execute_func)

    node.run_event_loop()
    node.finish_event_loop()
    #####

    time.sleep(10)

    print(node.event_q.qsize())
