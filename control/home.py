import control

""" reset the X/Y/Z/C axis to home state"""

if __name__ == "__main__":
    # 初始化运动控制实例
    controller = control.MoveControl(port='/dev/ttyUSB0', baudrate=115200)
    
    # 先稍向中心位置运动一端距离
    # speed = 15000  # 设置运动速度
    # controller.incremental_movement('X', -10, speed)
    # controller.incremental_movement('Y',  10, speed)
    # controller.incremental_movement('Z', -10, speed)
    
    # 回零操作
    controller.axis_homing('X')
    controller.axis_homing('Y')
    controller.axis_homing('Z')
    controller.axis_homing('C')
    
    # 关闭串口连接
    controller.close()