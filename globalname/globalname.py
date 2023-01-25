    @commands.is_owner()
    @commands.guild_only()
    @commands.command()
    async def globalrename(self, ctx, user: discord.Member, *, nickname):
        """Rename a member globally, in all servers."""

        for g in self.bot.guilds:
            if member:= g.get_member(user.id):
                try:
                    await member.edit(nick=f"{nickname}")
                    await ctx.send(
                embed=discord.Embed(
                    description=f":white_check_mark: ┃ Changed ``{user}``'s name in {g} to ``{nickname}``.",
                    color=0x46d539,
                ))
                    await ctx.tick()
                except Exception:
                    await ctx.send(
                embed=discord.Embed(
                    description=f":x: ┃ Could not change ``{user}``'s name in {g}",
                    color=0xD53946)
                )
