def pop_target(self, df, target_col):
    self.df = df
    self.target_col = target_col
    self.target = df[target_col]
    self.df = df.drop(columns=[target_col])
    return self.df, self.target