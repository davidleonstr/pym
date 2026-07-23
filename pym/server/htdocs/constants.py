EXAMPLECODE = r'''
<span class="tag">&lt;!py</span><br/>
userRole = GET.get(<span class="string">'role'</span>, <span class="string">['Guest']</span>)[0]<br/>
<br/>
<span class="keyword">def</span> <span class="keyword">StatusBadge</span>(color):<br/>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">return</span> (<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;span</span> <span class="keyword">style</span>=<span class="string">"color: {color};"</span><span class="tag">&gt;</span><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Active<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;/span&gt;</span><br/>
&nbsp;&nbsp;&nbsp;&nbsp;)<br/>
<br/>
header = (<span class="tag">&lt;h2&gt;</span>Welcome back, '{userRole}'!<span class="tag">&lt;/h2&gt;</span>)<br/>
<span class="tag">!&gt;</span><br/>
<br/>
<span class="tag">&lt;div</span> <span class="keyword">class</span>=<span class="string">"profile-card"</span><span class="tag">&gt;</span><br/>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;!=</span> header <span class="tag">!&gt;</span><br/>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;p&gt;</span>Status: <span class="tag">&lt;!=</span> StatusBadge(<span class="string">'#4ade80'</span>) <span class="tag">!&gt;&lt;/p&gt;</span><br/>
<span class="tag">&lt;/div&gt;</span>
'''