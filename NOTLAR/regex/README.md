# Regular expression 
```
nokta tüm ifadeleri gösterir eğer noktayı görmek istersek \. şeklinde bir kullanım yapmamız gerekir
```
```
 /(){}: gibi karakterler için yine ters slash kullanmak gerekir mesela \( 

```

```
sıralı özel karakterler için , herbir karakter için bir tane ters sslash kullanmak gerekir mesela
aramak istediğimiz {{ bu olsun , \{\{ şeklinde kullanmamız gerekir
```

```
\d --> 0 ile 9 arasındaki rakamları görür
\D --> küçük d nin vermedigi herşey
\w --> harfleri sayilari ve alt çizgiyi hep beraber gösterir
\W --> kücük w nin değili
\s --> boşlukları
\S --> bosluk harici herşey
```

```
\b --> sınır belirler mesela " semih asemih" ifadesinde \bsemih yazarsam basında a yazan kısmı almaz
string sınırı belirtiyor asemih ifadesinde a yerine - olsaydı semihi seçerdi
```
```

^ ifadesi satır başlancına göre seçer mesele ^sem yazdıysam başlangıcı sem olanları seçer
$ ifadesi satir sonuna bakıyor  ^ ifadesinin tersi gibi
```
## Gruplama
```
[] içerisine yazılan rakamları tek tek gösterir mesela 123 yazıyorsa direk 123 sayısını aramaz 1 2 ve 3 rakamlarını gösterir
- tüm karakterler için geçerli sayı degil sadece
gruplandırma mantıgı vardır
- mesela [0-9] bu ifade 0 ile 9 arasındaki rakamları gösteriyor , harf içinde aralık belirtebiliriz a-z arasında
[^1-4] ifadesinde başa gelen ^ karakteri değili anlamında kullanılıyor yani 1 ile 4 arasında olmayan sayıları ve herşeyi gösterir.
```
## Miktar Belirtme
```
\d\d\d\d\d ifadesi bize 5 rakamı gösterir bunun yerine \d{5} ifadesi aynı işlevi görür/
bir veya daha fazla karakter için + kullanılır
```
```
\d{2} ifadesi iki rakamlı sayıları ifade ediyordu \d{2,5} yazarsamda 2 ,3 ,4,5 rakamlı sayıları ifade eder
```
```
\d{6,} ifadesi 6 ve sonrasını kabul eder
ab* ifadesi bnin önünde bir veya birden fazla b yi gösterir
```