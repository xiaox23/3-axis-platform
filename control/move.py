import control

""" control X/Y/Z to specific position with specific speed """

if __name__ == "__main__":
     # 初始化运动控制实例
    controller = control.MoveControl(port='/dev/ttyUSB0', baudrate=115200)
    
    # 增量运动示例
    speed = 15000  # 设置运动速度
    
    # X axis
    # controller.incremental_movement('X', -30, speed)  # x前进
    # controller.incremental_movement('X', 10, speed)  #  x后退
  
#     # Y axis
#     # controller.incremental_movement('Y', -20, speed)  # y右移
#     controller.incremental_movement('Y',  20, speed)  # y左移
    
#     # Z axis
    # controller.incremental_movement('Z', 10, speed)    # z向下移动
#     controller.incremental_movement('Z', -20, speed)    # z向上移动
    
    # C axis
    controller.incremental_movement('C', -2.4, 0.01*speed)  # c轴逆时针旋转
    # controller.incremental_movement('C', 2.4, 0.01*speed)  # c轴顺时针旋转


    # 关闭串口连接
    controller.close()