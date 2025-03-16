import control 

""" get the information about the X/Y/Z axis """

if __name__ == '__main__':
    # 初始化运动控制实例
    controller = control.MoveControl(port='/dev/ttyUSB0', baudrate=115200)
    
    
    # 获取轴位置信息
    controller.get_axis_position('X')
    controller.get_axis_position('Y')
    controller.get_axis_position('Z')
    
    
    # 关闭串口连接
    controller.close()