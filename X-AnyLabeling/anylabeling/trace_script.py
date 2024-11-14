import trace

# 创建 Trace 对象，trace.Calls 选项表示跟踪所有调用
tracer = trace.Trace(trace=1, count=0)

tracer.run('exec(open("anylabeling/app.py").read())')
'''
# 打开一个文件以写入跟踪输出
with open("trace_output.txt", "w") as output_file:
    # 运行 example.py 脚本，并将输出重定向到文件
    tracer.run('exec(open("app.py").read())', output = output_file)
'''