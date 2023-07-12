# 轻舟智能车上位机

远程调度系统

___

## 主面板

![swj](swj_mianban.jpg)

## 功能介绍

上位机系统与轻舟机器人 ROS 之间，采用 TCP\IP 协议通信，无线传输。上位机为 server
端，轻舟机器人 ROS 端为 client。
上位机系统将下一个目标地点发送给轻舟机器人，若轻舟机器人行驶过程中调度系统检
测到可能发生碰撞，则需要单独向小车发送通行/禁行指令。轻舟机器人能够实时上报
自身位姿信息和状态信息以及摄像头实时图像，频率为 20HZ。

## 关于
<html>
    <head>
        <style>
            p { color:#FF23CC; }
            about{font-family: "方正喵呜"; }
            body{font-family: "幼圆"; }
            h1 {color: #ff3400;}
        </style>
    </head>
    <about>
        <h3>智能车调度软件 v1.0</h3>
        <p>参赛队伍: 风驰电掣</p>
        <p>所属学校: 华北电力大学(保定)</p>
        <p>要了解更多信息，请访问<a href="https://github.com/zhengyinloong/qingzhou_shangweiji">https://github.com/zhengyinloong/qingzhou_shangweiji</a></p>
    </about>
</html>