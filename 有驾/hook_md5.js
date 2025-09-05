{
    onEnter(log, args, state) {
        this.args0 = args[0];    // 入参
        this.args2 = args[2];    // 返回值指针
    },
    onLeave(log, retval, state) {
        var ByteArray = Memory.readByteArray(this.args2, 16);
        var uint8Array = new Uint8Array(ByteArray);

        var str = "";
        for (var i = 0; i < uint8Array.length; i++) {
            var hextemp = (uint8Array[i].toString(16))
            if (hextemp.length == 1) {
                hextemp = "0" + hextemp
            }
            str += hextemp;
        }
        log(`CC_MD5(${this.args0.readUtf8String()})`);       // 入参
        log(`CC_MD5()=${str}=`);                                                    // 返回值
    }
}