from cube import Cube


def cubeReto():
    cubo = Cube(3, 3, 3)

    for row in range(cubo.get_height()):
        for column in range(cubo.get_width()):
            for depth in range(cubo.get_depth()):
                cubo[row][column][depth] = f'[file {row}, columna {column}, casilla {depth}]'

    print(cubo)


def run():
    cubeReto()

    
if __name__ == '__main__':
    run()
