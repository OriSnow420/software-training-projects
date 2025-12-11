namespace client;

public class State(Config config, int x, int y)
{
  public Config Config { get; init; } = config;

  public int X { get; init; } = x;

  public int Y { get; init; } = y;

  public override string ToString()
  {
    var result = "";
    if (Config.WithBoarder)
    {
      result += new string('-', Config.Width + 2) + '\n';
    }
    for (var i = 0; i < Config.Height; ++i)
    {
      var line = new string(' ', Config.Width);
      if (i >= Y && i < Y + Config.PersonHeight)
      {
        line =
          (Config.WithBoarder ? "|" : "")
          + new string(' ', X)
          + Config.Person[i - Y]
          + new string(' ', Config.Width - X - Config.PersonWidth)
          + (Config.WithBoarder ? "|" : "");
      }
      result += line;
    }
    if (Config.WithBoarder)
    {
        result += new string('-', Config.Width + 2) + '\n';
    }

    return result;
  }
}

public class Config
{
  public int Width { get; init; } = 40;
  public int Height { get; init; } = 10;

  public List<string> Person { get; init; } = [" O ", "/|\\", "/ \\"];

  public int PersonWidth => Person[0].Length;
  public int PersonHeight => Person.Count;

  public bool WithBoarder { get; init; } = true;
}