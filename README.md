# Zen_of_Algotithm_recurrence_n_recursion

Practice code in the book with Python.

## 筆記

### 1.1 觀念

1. 遞推（recurrence）：此處定義為「立足於當下已知資料，向著目標推導出下一步結果」。
2. 遞迴（recursion）：此處定義為「一開始並不知道當下的結果，需要等待用來建構結果的基礎資料都收集上來後，才能得到當下的結果」。

### 1.2 實作

| 方案 | 特點 |
| ---- | ---- |
| 以遞推程式碼實作遞推程式碼 | 中規中矩，利用 Loop statement，有時候會加入 queue。|
| 以遞迴程式碼實作遞推程式碼 | 自上而下的遞迴程式碼，可以簡化程式碼。|
| 以遞迴程式碼實作遞迴程式碼 | 順理成章，函式／方法呼叫自己；自下而上，結果對齊。|
| 以遞推程式碼實作遞迴程式碼 | 利用 Loop statement 加上 stack，以避免 call stack overflow。|

註：自一個已排序過的數列建立二元樹時，若中點左右兩邊的子段落長度相差不超過 1，則建構出來的一定為平衡樹；又因此數列已被由小到大排序完畢，因此左子樹的節點數值，一定比中點值小，而右子樹的節點數值，一定比中點值大，此結果即滿足二元搜尋樹的定義。
