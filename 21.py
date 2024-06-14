import pandas as pd
order_data = pd.DataFrame({
&#39;CustomerID&#39;: [1, 2, 1, 3, 2],
&#39;OrderDate&#39;: [&#39;2022-01-01&#39;, &#39;2022-01-02&#39;, &#39;2022-01-01&#39;, &#39;2022-01-03&#39;, &#39;2022-01-02&#39;],

&#39;ProductName&#39;: [&#39;ProductA&#39;, &#39;ProductB&#39;, &#39;ProductA&#39;, &#39;ProductC&#39;, &#39;ProductB&#39;],
&#39;OrderQuantity&#39;: [3, 5, 2, 1, 4]
})
total=order_data.groupby(&#39;CustomerID&#39;)[&#39;OrderDate&#39;].count()
avg=order_data.groupby(&#39;ProductName&#39;)[&#39;OrderQuantity&#39;].mean()
earliest=order_data[&#39;OrderDate&#39;].min()
latest=order_data[&#39;OrderDate&#39;].max()
print(total)
print(avg)
print(earliest)
print(latest)
