object Test2 {
  def main(args: Array[String]): Unit = {
   import scala.collection.immutable.HashMap
   var a:Map[String,Int]=HashMap("a"->1)
    print(a("a"))
//    元组
    var aa=("a","b","c")

    var l=List(1,2,3,4,5)
    l= l.map(z=>z+2)


    print(l.toList)
  }
}
