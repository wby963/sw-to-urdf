# sw-to-urdf
**将四足机器狗骨架sw模型转为urdf模型，可在rviz显示**
- go urdf 为sw文件直接转为ros可用的urdf包
- src为基于ros可用的urdf所构建的适用于ros2的urdf包
-       launch中构建了启动文件，display一键启动rviz2，simulation启动gazebo未成功
-       meshes为STL文件，未更改
-       rviz为rviz配置文件
-       urdf中是机器人的urdf文件，test用于测试，urdf_SLDASM为正式使用的文件，稍作更改，robot为gazebo用，未成功
- solidworks 内含有图纸，标准sw文件，自己绘制的sw文件
