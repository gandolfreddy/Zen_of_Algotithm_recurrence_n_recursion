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

1. 自一個已排序過的數列建立二元樹時，若中點左右兩邊的子段落長度相差不超過 $1$，則建構出來的一定為平衡樹；又因此數列已被由小到大排序完畢，因此左子樹的節點數值，一定比中點值小，而右子樹的節點數值，一定比中點值大，此結果即滿足二元搜尋樹的定義。

2. 如何理解「應用『二分法』遞迴時，當處理資料量規模為 $n$ 時，時間複雜度／遞迴深度為 $O(log(n))$／$log(n)$」（log 以 $2$ 為底）？

    * 假設目前有一數列，其中含有 16 個大小已排序好的數字。
        $11, 12, 12, 15, 21, 21, 23, 26, 31, 32, 32, 34, 37, 41, 44, 46$
    * 若要在此數列中，找到 $44$，並應用二元搜尋方式尋找，則過程如以下所示：

        ```Python
        ## 中點索引值 mid 為 (0 + 15) // 2 = 7，因此中點值為 26。

        [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]
        11, 12, 12, 15, 21, 21, 23, 26, 31, 32,  32,  34,  37,  41,  44,  46
        ##                           ↑
        ##                           1
        ##------ non-44 section -----|
        ```

        ```python
        ## 中點索引值 mid 為 (7 + 15) // 2 = 11，因此中點值為 34。

        [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]
        11, 12, 12, 15, 21, 21, 23, 26, 31, 32,  32,  34,  37,  41,  44,  46
        ##                           ↑                 ↑
        ##                           1                 2
        ##--------------- non-44 section --------------|
        ```

        ```python
        ## 中點索引值 mid 為 (11 + 15) // 2 = 13，因此中點值為 41。

        [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]
        11, 12, 12, 15, 21, 21, 23, 26, 31, 32,  32,  34,  37,  41,  44,  46
        ##                           ↑                 ↑         ↑
        ##                           1                 2         3
        ##-------------------- non-44 section -------------------|
        ```

        ```python
        ## 中點索引值 mid 為 (13 + 15) // 2 = 14，因此中點值為 44，找到目標值。

        [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]
        11, 12, 12, 15, 21, 21, 23, 26, 31, 32,  32,  34,  37,  41,  44,  46
        ##                           ↑                 ↑         ↑    ↑   
        ##                           1                 2         3    4
        ##-------------------- non-44 section -------------------|
        ```

    * 根據上述內容，可以得知，欲於長度為 16 的數列中，搜尋到特定數字，因每次都是從數列中央，對半切割搜尋，因此基本上最多花費 4 次的搜尋次數，即找到我們的目標。其關係可以描述成以下數學式：

        $16 * (\frac{1}{2})^4 = 1$

        若我們將代表數列長度的 $16$ 替換成 $n$，與代表花費的搜尋次數 $4$ 替換成 $k$，則可表示成：

        $n * (\frac{1}{2})^k = 1$

        接著我們就可以將此式子逐步轉換成，只有 $k$ 在其中一側的等式：

        $\frac{n}{2^k} = 1$

        $2^k * \frac{n}{2^k} = 2^k$

        $n = 2^k$

        $\log{2}(n) = \log{2}(2^k)$

        $\log{2}(n) = k$

        最終得：

        $k = \log{2}(n)$

        又因於電腦科學中，對數習慣以 2 為底來表示，因此也可寫成：

        $k = \log{2}(n) = \log(n)$

        即代表資料規模為 $n$ 的已排序數列，在其中尋找一數時，花費的搜尋次數為 $k$。

3. 若遇到應用遞迴撰寫程式時，達到 call stack 的最大允許深度，則會出現錯誤。可使用以下技巧，讓「壞」遞迴變成「好」遞迴：
    * 利用編譯器／直譯器針對「尾遞迴」的最佳化（tail-call optimization, TCO），重構原程式。
        * 尾遞迴（tail-recursion）：遞迴呼叫發生於函式的最後，且必須是單純的遞迴呼叫，不能再進行其他的動作，例如不可為 `return lt[cur] + sum_next(lt, cur + 1)`。

            ```python
            def sum_next(lt, i):
                if i == len(lt): return
                sum += lt[i]
                sum_next(lt, i+1)
            ```

        * 非尾遞迴

            ```python
            def fibonacci(n):
                if n <= 0: return 0
                return fibonacci(n-1) + fibonacci(n-2)
            ```

    * 從演算法方面著手（例如二分法），將遞迴深度控制在合理範圍內。
