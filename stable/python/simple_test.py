#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单测试：验证引擎核心功能
"""
import sys
import os

# 确保可以导入board模块
sys.path.insert(0, os.path.dirname(__file__))

print("测试1: 导入模块...")
try:
    from board import board, common_20210604_fixed as common, library
    print("✓ 模块导入成功")
except Exception as e:
    print(f"✗ 模块导入失败: {e}")
    sys.exit(1)

print("\n测试2: 创建棋盘...")
try:
    B = board.Board()
    print("✓ 棋盘创建成功")
except Exception as e:
    print(f"✗ 棋盘创建失败: {e}")
    sys.exit(1)

print("\n测试3: 初始化映射...")
try:
    mapping = B.translate_mapping(B.mapping)
    print(f"✓ 映射初始化成功 (共{len(mapping)}个暗子)")
except Exception as e:
    print(f"✗ 映射初始化失败: {e}")
    sys.exit(1)

print("\n测试4: 创建初始局面...")
try:
    from musesfish_pvs_20210604_fixed import Position, initial_covered
    pos = Position(initial_covered, 0, True, 0).set()
    print("✓ 初始局面创建成功")
    print(f"  - 棋盘大小: {len(pos.board)}")
    print(f"  - 红方行棋: {pos.turn}")
except Exception as e:
    print(f"✗ 局面创建失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n测试5: 生成合法走法...")
try:
    moves = list(pos.gen_moves())
    print(f"✓ 生成走法成功 (共{len(moves)}个合法走法)")
    if len(moves) > 0:
        print(f"  - 示例走法: {moves[0]}")
except Exception as e:
    print(f"✗ 生成走法失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n测试6: 评估局面...")
try:
    score = pos.score
    print(f"✓ 局面评估成功 (分数: {score})")
except Exception as e:
    print(f"✗ 局面评估失败: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("✓ 所有核心功能测试通过！")
print("="*50)
print("\n引擎可以正常使用。")
print("运行完整引擎: python musesfish_pvs_20210604_fixed.py")


