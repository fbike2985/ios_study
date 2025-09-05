{
  onEnter(log, args, state) {
    // 获取输入数据的指针和长度
    this.inputPtr = args[0];         // 输入数据指针
    this.inputLen = args[1].toInt32(); // 输入数据长度
    this.outputPtr = args[2];        // 输出指针

    // 将输入数据读取为字节数组
    const inputByteArray = Memory.readByteArray(this.inputPtr, this.inputLen);

    // 尝试读取为 UTF-8 字符串
    const inputString = Memory.readUtf8String(this.inputPtr, this.inputLen);

    log(`CC_MD5 called with input: ${inputString}`); // 打印原始字符串内容
  },

  onLeave(log, retval, state) {
    // 读取返回值（输出指针中的 MD5 哈希结果）
    const ByteArray = Memory.readByteArray(this.outputPtr, 16);
    const uint8Array = new Uint8Array(ByteArray);

    // 转换哈希值为十六进制字符串
    let str = "";
    for (let i = 0; i < uint8Array.length; i++) {
      let hextemp = uint8Array[i].toString(16);
      if (hextemp.length == 1) {
        hextemp = "0" + hextemp; // 确保每个字节以两位十六进制表示
      }
      str += hextemp;
    }

    // 打印返回值
    log(`CC_MD5() returns: ${str}`);
  }
}