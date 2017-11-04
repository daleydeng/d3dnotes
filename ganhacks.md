- ls-gan 训练速度快，有时不稳定，会触底反弹。噪点多。
- alphfa-gan 中code discriminator 可以用样本估计的均值和方差对应的高斯KLD散度距离替换gan距离，效果更好。因为code是已知高斯分布，
所以可以用已知分布的距离度量来衡量。而GAN距离适用于未知分布的距离度量，如样本。改进后的alphagan训练流程，通过训练过程中重构误差和分布误差的减小，将x_real和z_real两空间捏合到一起。也通过重构误差的逐渐减小，将远离的gan loss拉回到正常范围。
  1. 更新D, 最小化GAN loss
  2. 更新Q,最小化x_rec, kl_loss。注意z_rec与x_rec有冲突，只能放弃z_rec，此布目的是让Q随动G, 保证G专注训练GAN误差使得生成图像质量较高
  3. 更新G, 最小化GAN loss. 专注生成高质量的图像。
- wgan-gp 似乎更稳定。learning rate 不能太大，一般为1e-4,适用于D和G。gradient penalty 可用离散梯度替代。训练效果更加刚性，由大结构变为细粒度的小结构。噪点少。
