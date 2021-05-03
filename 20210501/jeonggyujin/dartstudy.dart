// is -> 이 타입이 이 타입이 맞는가?
// is 키워드 : 같은 타입이면 true를 반환하고 다른 타입이면 false를 반환.
// is! 키워드 : 같은 타입이면 false를 반환하고 다른 타입이면 true를 반환.

// https://blockdmask.tistory.com/394 as, is, 클래스에서 다운캐스팅, 업캐스팅 사례
/*
void main() {
  int a = 20;
  if (a is int) {
    print('a is int type');
  } else {
    print('a is not int type');
  }
}

// as -> 데이터 타입을 다른 타입으로 변환 = typedef

void main(){
  int a = 33;
  int b = a as int;
  String str = "as keyword example";
  String copyStr = str as String;
}
*/

// https://medium.com/hongbeomi-dev/dart-%EA%B8%B0%EB%B3%B8-%EB%AC%B8%EB%B2%95-1b54cdb83b09 다트 문법

// 접근지정자 _ = 변수앞에 _를 붙이게되면, 해당 변수를 private변수로 지정
class Person {
  String name;
  int _age;

  int get age => _age;
  set age(int value) => _age = value;
}

void main() {
  var person = Person();
  print(person.age); // age = null
  person.age = 1;
  print(person.age); // age = 1
}

/* 
<List = 변수선언의 한 형태1>
List<String> items = ['고양이', '강아지', '호랑이'];
var items = ['고양이', '강아지', '호랑이']; // 위와 동일함.
*/

/*
<Map = 변수선언의 한 형태2>
Map<String, String> personMap = { 
  'hongbeom' : 'hi',
  'gildong' : 'hello'
};
var personMap = { 
  'hongbeom' : 'hi',
  'gildong' : 'hello'
};

<Set = 변수선언의 한 형태3> 
Set<String> personSet = {'hongbeom', 'gildong'};
var personSet = {'hongbeom', 'gildong'};
print(personSet.contains('hongbeom'); // true

<비어있는 Set이나 Map을 작성할 경우 값 없이 그냥 {} 만 작성하면 Set이 아닌 Map으로 인식>
var mySet = <String>{}; // Set<String>
var mySet2 = {}; // Map<dynamic, dynamic>으로 취급

<where 는 조건을 필터링할 때 사용하는 함수>
final items = [1, 2, 3, 4, 5];
items.where((e) => e % 2 == 0).forEach(print); // 2, 4

<forEach() 함수는 (E element) {} 형태의 함수를 인수로 받는다.>
final items = [1, 2, 3, 4, 5];
items.forEach((e) {
  print(e);
}); // 1, 2, 3, 4, 5
items.forEach((e) => print(e)); // 1, 2, 3, 4, 5
items.forEach(print); // 1, 2, 3, 4, 5

<?. 연산자를 사용하여 null 여부를 판단>
String name = null;
print(name?.length); // null
print(name?.length ?? 'hongbeom'); // hongbeom

함수를 정의할때 매개변수에 {}로 씌우는 경우가 있는데, 이런 매개변수를 Named Parameter라고 부른다
void something(String name, {int age = 10}) {} //age라는 변수는 불충분해도,  함수가 성공한다
void main() {
  something('안홍범', age: 26); // age = 26
  something('안홍범'); // age = 10
  something(age: 26); // error 필수 매개변수를 입력하지 않았다.
  something(); // error 마찬가지
}

with = 상속하지 않고 다른 클래스의 기능을 가져오거나 오버라이드 할수있음
class Cat implemets Animal {
  
  @override
  void eat() {
    print("고양이가 음식을 먹습니다")
  }
  
}
class PersianCat extends Cat with Biology {
  
}


*/
