-- For ipynb output: one markdown cell per heading, and plain markdown images
-- (no <figure> HTML) so VS Code/Jupyter render them reliably.
if not FORMAT:match("ipynb") then return {} end

local function is_cell(b)
  return b.t == "Div" and b.classes:includes("cell")
end

function Figure(fig)
  -- replace a captioned figure with a bare image paragraph
  local img
  fig:walk({ Image = function(i) img = img or i end })
  if img then
    img.caption = {}
    return pandoc.Para({ img })
  end
end

function Pandoc(doc)
  local out, buf = {}, {}
  local function flush()
    if #buf > 0 then
      table.insert(out, pandoc.Div(buf, pandoc.Attr("", { "cell", "markdown" })))
      buf = {}
    end
  end
  for _, b in ipairs(doc.blocks) do
    if is_cell(b) then
      flush(); table.insert(out, b)
    else
      if b.t == "Header" and b.level <= 2 then flush() end
      table.insert(buf, b)
    end
  end
  flush()
  doc.blocks = out
  return doc
end
