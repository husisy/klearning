# 量子力学

1. 参考书
   * @book-曾谨言-量子力学
   * @book-朗道-量子力学（非相对论理论）
2. 基本対易关系$[ x_i,p_j ] =i\hbar \delta _{ij}$
3. 复共轭，转置，厄米
   * $(\phi_1, O\phi_2)^*=(\phi_1^*, O^*\phi_2^*)=(O\phi_2, \phi_1)$
   * $(\phi_1,O^T\phi_2)=(\phi_2^*,O\phi_1^*)$
   * $(\phi_1,O^{\dagger}\phi_2)=(O\phi_1,\phi_2)$
   * $O^{\dagger}=(O^T)^*$
4. 算符关系
   * $\left[ A,BC \right] =B\left[ A,C \right] +\left[ A,B \right] C$
   * Jacobi恒等式：$\left[ A,\left[ B,C \right] \right] +\left[ B,\left[ C,A \right] \right] +\left[ C,\left[ A,B \right] \right] =0$
5. Levi-Civita symbol
   * $\epsilon_{ijk}\epsilon_{imn}=\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km}$
   * $\epsilon_{ijk}\epsilon_{ijm}=2\delta_{km}$
   * $\epsilon_{ijk}\epsilon_{ijk}=6$
6. 角动量与角动量分量算符
   * 定义式：$L_i=\epsilon_{ijk}x_jp_k=\epsilon_{ijk}p_kx_j$, $L_{\pm}=L_x\pm iL_j$
   * $L_iL_i=L_xL_x+L_yL_y+L_zL_z=L_zL_z+L_{\pm}L_{\mp}\mp \hbar L_z$
   * 対易关系：$i\hbar L_i=\epsilon_{ijk}L_jL_k$
   * $\left[ L_i,L_j \right] =i\hbar \epsilon_{ijk}L_k$, $\left[ L_i,x_j \right] =i\hbar \epsilon _{ijk}x_k$, $\left[ L_i,p_j \right] =i\hbar \epsilon_{ijk}p_k$
   * $\left[ L_+,L_- \right] =2\hbar L_z$, $\left[ L_z,L_{\pm} \right] =\pm \hbar L_{\pm}$
   * $\left[ L_iL_i,L_j \right] =0$, $\left[ L_i,x_jx_j \right] =0$, $\left[ L_i,p_jp_j \right] =0$
7. 球坐标系下动能算符 $(r,\theta ,\phi)$
   * $L_z=-i\hbar \frac{\partial}{\partial \phi}$
   * $L_{\pm}=e^{\pm i\phi}\left( \pm \frac{\partial}{\partial \theta}\pm i\cot \theta \frac{\partial}{\partial \phi} \right)$
   * $L_iL_i=-\hbar ^2\left( \frac{1}{\sin \theta}\frac{\partial}{\partial \theta}\sin \theta \frac{\partial}{\partial \theta}+\frac{1}{\sin ^2\theta}\frac{\partial ^2}{\partial \phi ^2} \right)$
   * $\nabla ^2=\frac{1}{r^2}\frac{\partial}{\partial r}r^2\frac{\partial}{\partial r}+\frac{1}{r^2\sin \theta}\frac{\partial}{\partial \theta}\sin \theta \frac{\partial}{\partial \theta}+\frac{1}{r^2\sin ^2\theta}\frac{\partial ^2}{\partial \phi ^2}$
   * 径向动量 $p_r=-i\hbar \left( \frac{\partial}{\partial r}+\frac{1}{r} \right)$, $p_{r}^{\dagger}=p_r$, $p_{r}^{2}=-\hbar ^2\frac{1}{r^2}\frac{\partial}{\partial r}r^2\frac{\partial}{\partial r}$
   * 动能 $T=\frac{p_{r}^{2}}{2m}+\frac{L_iL_i}{2mr^2}$
8. 厄米性要求波函数周期性
   * $L_z$: $\frac{1}{\sqrt{2\pi}}e^{im\phi}$
   * $p$: $\frac{1}{\sqrt{2\pi \hbar}}e^{ip\cdot r}$
9. 概率守恒
   * 粒子密度 $\rho =\psi ^*\psi =\sum_i{\delta \left( r-r_i \right)}$
   * 流密度算符 $j=\frac{1}{2m}(\psi^*p\psi -\psi p\psi^*) =\frac{1}{2m}\sum_i{\left( p_i\delta(r-r_i) +\delta (r-r_i) p_i \right)}$
   * $\partial _t\rho +\nabla \cdot j=0$
10. 不确定度关系
    * $\left( \xi A\psi +iB\psi ,\xi A\psi +iB\psi \right) \ge 0$
    * $\Delta A=\overline{A^2}-\overline{A}^2$
    * $\Delta A\Delta B\ge \frac{1}{2}\left| \overline{\left[ A,B \right] } \right|$
    * 区别于测不准关系
11. 球谐函数
    * $Y_{l}^{m}\left( \theta ,\phi \right) =\left( -1 \right) ^m\sqrt{\frac{\left( l-m \right) !}{\left( l+m \right) !}\frac{2l+1}{4\pi}}P_{l}^{m}\left( \cos \theta \right) e^{im\phi}$
    * $-l\le m\le l$
    * $\left( Y_{l}^{m} \right) ^*=\left( -1 \right) ^mY_{l}^{-m}$
    * $Y_l^m$的宇称是$(-1)^l$
    * $L^2|lm\rangle =l\left( l+1 \right) \hbar ^2|lm\rangle$, $L_z|lm\rangle =m\hbar |lm\rangle$
    * $(L_+)_{mn}=\sqrt{(l+m)(l+1-m)}\delta_{m,n+1}\hbar$
    * $(L_-)_{mn}=\sqrt{(l+n)(l+1-n)}\delta_{m+1,n}\hbar$
    * $l=\frac{1}{2}$: $L_i=\frac{1}{2}\hbar \sigma_i$
    * $l=1$：`L_plus=diag(sqrt(2)*ones(1,2), 1)*hbar`
    * 角动量选择定则（没看懂）
12. $\delta \left( x-x_0 \right) =\frac{1}{2\pi}\int_{-\infty}^{\infty}{e^{ik\left( x-x_0 \right)}dk}$
13. 対易力学量完全集complete set of commuting obserables (CSCO)
14. 非简并定态波函数都是实函数 $\langle L \rangle = \langle p \rangle=0$（时间反演对称性）
15. Pauli matrix
    * $\left[ \sigma _i,\sigma _j \right] =2i\epsilon_{ijk}\sigma_k$
    * $\left\{ \sigma_i,\sigma_j \right\} =2\delta _{ij}$
    * $\sigma_i\sigma_j=\delta_{ij}+i\epsilon_{ijk}\sigma_k$
    * $( \sigma \cdot a ) ( \sigma \cdot b ) =a\cdot b+i\sigma \cdot \left( a\times b \right)$
    * $\sigma_{\alpha \beta}\cdot \sigma_{\mu \nu}=2\delta_{\alpha \nu}\delta_{\beta \mu}-\delta_{\alpha \beta}\delta_{\mu \nu}$
    * $\exp \left\{ i\theta \hat{n}\cdot \sigma /2 \right\} =\cos \frac{\theta}{2}+i\hat{n}\cdot \sigma \sin \frac{\theta}{2}$
16. 旋量：$\psi_1=\psi^2$, $\psi_2=-\psi^1$, $\psi^{\lambda}\phi_{\lambda}=-\psi_{\lambda}\phi^{\lambda}$, $\psi^{\lambda}\psi_{\lambda}=0$
17. 基矢变换 @book-李新征-群论-P195
    * $\left[ e_1,e_2,\cdots ,e_f \right] =\left[ f_1,f_2,\cdots ,f_n \right] \left[ P \right]$
    * $\left[ x \right]_f=\left[ P \right] ^{-1}\left[ x \right]_e$
    * $\left[ A \right]_f=\left[ P \right] ^{-1}\left[ A \right]_e\left[ P \right]$
    * 欧拉角$\left[ C_{z2}(\gamma) C_{y1}(\beta) C_{z0}(\alpha) \right]_{x0y0z0}=R_z(\alpha)R_y(\beta)R_z(\gamma)$
18. 动力学方程 $\frac{d}{dt}\bar{A}=\frac{1}{i\hbar}\overline{\left[ A,H \right] }+\overline{\partial _tA}$
19. 位力定理Virial $2\overline{T}=\overline{r\cdot \nabla V}$
    * 谐振子势：$\overline{V}=\overline{T}$
    * 库仑势、delta势：$\overline{V}=-2\overline{T}$
20. 谐振子宇称$(-1)^n$
21. 哈密顿量$H$与厄米算符$F/G$满足対易关系$[H,F]=[H,G]=0$，$[G,F]=C$（非零常数），则体系所有能级简并且简并度无穷大
22. Ehrenfest定理 $m\frac{d^2\bar{r}}{dt^2}=-\overline{\nabla V}=\overline{F\left( r \right) }=F\left( \bar{r} \right)$
    * 波包很窄
    * $V$在空间中变化很缓慢
23. 对称变换 $\left[ Q,H \right] =0$, $QQ^{\dagger}=I$, $Q=I+i\epsilon F$, $F=F^{\dagger}$
    * 对称变换只能是幺正或者反幺正变换，连续对称变换只能是幺正变换，反幺正变换不存在守恒量
24. 平移变换$D(\delta) =\exp \{ -i\delta \cdot p/\hbar \}$, $D( \delta ) \psi ( r ) =\psi ( r-\delta )$
25. 转动变换
    * $R_{\hat{n}}\left( \delta \right) =\exp \left\{ -i\delta \hat{n}\cdot L/\hbar \right\}$
    * 作用于矢量 $R_{\hat{n}}\left( \delta \right) r=r+\delta \hat{n}\times r=\left( 1-i\delta \hat{n}\cdot s/\hbar \right) r$
    * 作用于函数 $R_{\hat{n}}\left( \delta \right) \psi \left( r \right) =\psi \left( r-\delta \hat{n}\times r \right)$
    * 作用于矢量函数 $R_{\hat{n}}( \delta ) \vec{A}(r) =\exp \{ -i\delta \hat{n}\cdot j/\hbar \} \vec{A}(r)$, $j=L+s$
26. 宇称算符：厄米性，与动量算符不対易
    * 奇偶宇称波函数 $\psi _{\pm}=\frac{1}{2}\left( 1\pm P \right) \psi$
    * 奇偶宇称算符 $A_{\pm}=\left( 1\pm PAP \right)$
27. 时间平移算符 $D\left( \delta_t \right) =\exp \left\{ -i\delta_tH/\hbar \right\}$

```latex
pass
```
