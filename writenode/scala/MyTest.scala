//参数就是属性，构造方法
class MyTest(a: Int,n:String){
  //就是this的别名
  self=>
  print("创建对象")
  //自动生成getset方法，scala的继承也会重写属性
  var aaa="shuxing"
  var _i:Int=_
  def i=_i
  def i_=(i:Int):Unit={
    self._i=i
  }
  //默认生成占位符
  var bbb:Int=_

  println(this.aaa)
  println(self.aaa)

  Console.print("aaa")
  Console print ("aaa")


  def setaaa(aaa:String): Unit ={
    this.aaa=aaa
  }


}

object MyTest {


  def main(args: Array[String]): Unit = {
    //选择不同的函数
    var data:Int=3
    def xxx()=data match {
      case 1=> "xxxx"
      case 2=> 2
      case _=>"ssss"
    }

    var zz=xxx
    println(zz)



    var test=new MyTest(1,"zlx")
    test.setaaa("dddd")
    println(test.aaa)

//    默认
    test._i;
    test._i=10
    //or


    //自定义
    test.i_=(10)
    test i_= 10
    test.i=10

    test.i;

  }
}
