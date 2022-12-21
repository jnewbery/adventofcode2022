def part1(ll):
    raise NotImplementedError

def part2(ll):
    raise NotImplementedError

TEST_INPUT = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

TEST_SOL = [26397]

FULL_INPUT = """<{({(([[<<([[([][])]{([]<>)([]<>)}]<[[[]{}]{()[]}]>)(<<[[]()][[]()]><[<>[]]<[]()>>>{<<<><>><<>[]>>[<[]<>><
{<[<((<<({([{{{}[]}<<><>>}]<<{[]<>}([]<>)>>)<{(<[]()>{()()})<(()<>){(){}}>}([(()[])<[]>][[[][]]{{}}])
<{[[{<[[{(<[[({}())[()()]]([<>()](<>()))][(([]<>)([][]))(({}{})[<><>])]><<<[[]<>][{}[]]>([<>{}
<[[<[([({[{<[({}<>)([]<>)](<<>[]>([]()))><[<[]{}>[<><>]]>}>[{[[({}<>)<()<>>][{{}[]}(()())]][[(<>{}){<>{
[((<{((([[<<<[<><>]{{}[]}>>(([<><>]<()[]>)<(()<>)>)>([[[{}{}][[][]>]<{<>()}[<>{}]>])]]<{[<[
([{([[[{(<({<<[]<>>[()()]>{(()[])}})<(<<{}()>(<>>>([(){}]))<[(<>{}){()}]((()[]){()()})>>>)}{
<{{[(<[<<[[{<(()[])>[[{}()]{{}[]}]}[[(<>())[()()]]{<{}{}>}]](<{[<><>]{{}{}}}<({}[])[<><>]>><{[{}<>](<><>)
{({<[<([[(({({<>()}{{}{}})})<<<((){})[[]()]><{{}()}[[][]]>>{(<{}{}>{{}()})}>)<<{<[{}[]][{}{}]>([[][]]{
{[(((((<{[({<{()[]}(()())>{<(){}>{{}()}}}(<[<>()]{[]()}>(<()()>{{}<>})))[<[[{}{}](<>()>]({[]<>
(([((<{<[((<{{<><>}{[]{}}}><<<<>>[{}]>([[]{}]<<>[]>)>)[[{<{}>{()()}}[[{}[]](()()>]](<<<>{}>[[]
{<([[{<{([[<([[]<>]({}{})){{{}()}({}[])}>](<(<()()><()[]>)<<[]<>>([]{})>>)]){[{<<[()[]]<<>{}>><({
<{[[([<<<(<{{(()<>)(()())}([{}<>]((){}))}>)>({({{{()<>}({}<>)}<[[]<>]{<>[]}>})(({<(){}>[<>[]]}<([]{})<[]{}>>)
(<{<{[[({(<[((<>[]){{}})<(<><>)<[]{}>>]((<<>[]><[]()>)<<{}{}>{(){}}>)>(<[[[]<>]]{{<>{}}{[]()}}>(<{
{(({{[[{<[((<<()<>>[{}{}]>((()<>){[]()})){{(<>{})[<>[]]}<<<><>>>}){{({<>{}}([]()))[{<><>}{[]
(([<(([({{<{[{()<>}<{}[]>]}{[[()()][()<>]}[{<>{}}({}{})]}>((<<<>{}>[<>()]>{{[]<>}({}{})}){[<{
[[{{(<<[[[[<<<<>{}>({}())>[([]<>)(()())]>]<<<{<>()}>[<<>[]>[()()]]>[([[]()]<[][]))<[<>{}]{{}<>
{[{(((([<[{([(()()){()()}][<(){}>[{}<>)])[(<{}<>>{<>()})({{}<>}[()[]])]}(<({[]<>}<()[]>)({[]<>
<<([(([{<{<<<[{}[]]((){})>((<>[])(()<>))>{{{<>()}{[]}}{([][])}}>[<{{<>[]}<<>>}({[]<>})>]]({({{<><>
[{((<{<[[<[{[{{}<>}]{[{}][<>[]]}}[<([]())<()[]>>((<>){[]{}})]]<{(<()<>><{}<>]){[[]<>]({}{})}}({<{}[]>{{}
<[<{(<[[<(((<({}[])><(<><>)(<>())]){{{()()}(<>())}<[{}()]>})[([[<>[]]{{}[]}]{{{}()}<{}[]>})[[(()<>){<>
[([{{[<([{[([[()<>]])([[<>][()[]]][[<>[]]<<>[]>])]}{([<<{}()>({})>(<[]()>(<><>))]<<{{}<>}{<>}><(<>
<<[[([([(<(<<[{}[]]<()[]]><{[]{}}[<>()]>>)>[<<({[][]}<<><>>)[<{}{}>{()<>}]><({<>{}}([]))((
<({<{(<[({([[{()}(<><>)](<[][]>[{}{}])](([[]<>]<<>{}>))){({<<>{}>[[]{}]}<([][])>)<<(<><>)<[]<>>}>}}((([[()<
{([<(<[(({[({[(){}]<<>{}>}[[{}{}][{}[]]])]{({[()<>]{()[]}}(<[][]>[()[]])){{{[]{}}(<>[])}[<(){}>(
<[<[<{[{<[{[<<{}<>>(<>)>]{<({}{}){(){}}>((<>{})[{}<>])}}[<[[<><>]{{}<>}]{<()()>}>{<<[]()>(()())>{{{}<
(({[[<<[({[{{<()()>}}{<[<>()]>}][(<{[][]}>{[{}()]{[]<>}})<{{<>{}}(()[])}{{[]()}<<>[]>}>]})
<((<([[({(<{[[(){}]<[][]>]}>({<[()<>](()[])>(([]<>)([]<>))}<{[[]<>]{(){}}}(<()<>>([][]])>))}<{[<[({}
{({{{[[{{[{(<<(){}>[{}{}]>((()<>)[<>{}]))[<<{}[]><[]>>[{{}{}}(<>[])]]}[(<<(){}>({}{}))((<>{})([]<>)))
[[(({[{(<({[{<[]()>{()[]}}<(<>())<()()>>]<(({}[]){{}<>])((()<>){{}[]})>}([[({}{})[<>()]][{<><>}]]{([[
[[{<[([<[((<([[]{}][{}<>])([{}<>])>[([()<>]{{}{}}){{[]()}}])<({{[]()}[[]()]))>)([<<<<>{}><{}()>><(<>
<<({{{<{[<{<{<[]<>>[[]{}]}[<[]()>{[]{}}]>[[[(){}][<><>]]{(<>[]}({}{})}]}><[[({{}[]}{[]()}){(<>())[()<
{{(({[[[{<[<(([]())([]{}))([{}{}](()[])}>]>}([<{[[[]()][(){}]]<{<>[]}>}({<()<>><[]<>>})>((([()
(<(({{(([(({{<{}[]>({}())}([<>[]][{}()])}((<[][]>{()<>}){[[]<>]<{}{}>}))<({{[]<>}([][])}{<[]{}>{<>[]}})
((([<([([{{{<<<>{}><{}[]>>[[<>[]][{}[]]]}}(([<<>{}>[()[]]][{{}{}}])(<[()()][<><>]>{{<>[]}})}}]<{[[<
{{(<[<[<[<<[[(<>[])]({<><>}[()()])]>>]>[{{[[{(<>[])([][])}{[[][]]([]())}]>[[[<{}{}>({}())]<{<>
<[{[[([[{[(<[<{}{}>{(){}}][{[]<>}<()[]]]>(([()<>][[][]]){[<>{}](()[])}))[[<<{}>[<>{}]>[({}{})({}{})]]<([[]{}
({<<<{<({{{{{[()()]({}())}[[[]{}][<><>])}({<()()><[]()>}({<>()}))}{(((<>()){()()}){<(){}><()[]>})(([{}()]
([<({[{({(<<{[{}()]}{{{}[]}((){})}>>)<<{[((){})[()]]}<<{[]<>}<<>()>>([<>()][[]<>])>>{<<[<>[]]<[]<>>)<{<
(<[<<(<[[[[{{({}<>)[{}{}]}<[[]{}]([]<>)>}][<[<<>{}>{[]}][[[]{}](<>())]><<[<>()][(){}]><{[]
(({[[(([<(([{({}[])[<>{}]}{(<>[])({}{})})<<<{}[]>({}())>[({}<>)<{}()>]>)[<<[[][]]((){})><{{}(
{[((<([<[{[{<[<><>][()()]><{<>{}}>}[{<[][]>[()<>]}<(<>())<()<>>>]]<<<(<>())<()[]>>>[{{{}[]}}[[{}()]((){
{{<{({{({[<((({}{}){<>[]}){<{}()>{<>[]}})>(<{<<>{}><[]<>>}>[[{[]<>>{<><>}]{((){})<(){}>}])]}(<{[{{<><>}{[
(({<[[{[(<(((({}{}){()<>}))<{{[]{}}{{}{}}}<[{}<>][(){}]>>)>[{{(<<><>>([]{}))[((){})<{}[]>]}}(([[<>()]{<>()}]
[<([[[<[<{<{<{[]{}}{[]{}}>[([]())<<>[]>]}({{[]{}}<[]()>}<({}())(<>{})>)>}[({[[{}[]][{}<>]]})]>]><[
<{[<<[[<{[[{<<{}[]>[<><>]>}({[[]{}]<{}()>}((()[])))]{[<{()}[[]{}]>]{(({}[])<{}()>)<(<>())[()<>]
[[([[{[[(([{[[<>()]{<>()}]({(){}}({}{}))}[<[<><>]([]())>(<[]()><{}[]>)]]{(<<<><>>[[]{}]>(<[][]>((){}))
{(<<[[{[{{(<<<{}[]>(<>[])>({[]{}}([]{}))>[{<<>()>[[]<>]]([{}[]])])}[[{(<<><>>[()()])<<<><>>>}([<<>
([((<(<[(<{((<{}{}>{<><>})){{(()[])[{}[]]}}}{[[[(){}][<><>]]]({<()<>>{{}[]}}<[()()]{()[]}>)}>[<{(<{}
[(<[([[({({<[{<>()}([]<>)][(<><>)<()[]>]>})[{([(())({}[])][{[]<>}<()<>>])}({<[{}{}](()())><({}())[<>[]
([(<<[<{<{((<(<>[])({}<>)>{{()()}<<>{}>}))<{[[()[]][()[]]][({}[])<{}()>]}{<({})><{[][]}{{}<>}>}>}<<<({(){}}
[(<{(([({<{{(<[]<>>({}()))}}[<[[{}[]][[]]]>[({[]<>}(<>{}))]]>})]<([(<([[()()][[][]]]<((){}
((({([(<<{{<<({}())(())>([<>()]<()()>)>}}<[(<{{}[]}<()<>>><({}{}){(){}}>)][(({()<>}([]()))([()]))({{{}()}
{<(({[<([{[({([][])[[]{}]}<({}<>)<<>()>>)<<{<>()}{[]<>}>{{{}}{[]()}}>]}])<<{<(([[]{}]<<>[]>)){<<[]<>>><<()[
[{<(<<<((<<<{[()<>]{[]<>}}>[[<{}{}>[()[]]]<(<><>)[()[]]>]>{[[[[]()][<>[]]]]({(<>}{[]{}}})}>){({
<<[((<<[{{[(<[<>()]><{{}[]}{<>{}}>){[(()[])([]())][[(){}][{}[]]]}]([<[[][]]{(){}}><<{}{}>{<>{}}>][[
{<<{<<{<({[[([<>{}])[{[]<>}{{}[]}]][[<()<>>[<>{}]]]]<([{[]()}({}{})]({[]()}{<>()})){[({}<>)[[]{}
{<<[{((([<([[<[]()><<><>>][{()<>}<[][]>]]{<[{}[]][()[]]>[{<>{}>{[]}]}){[([[]{}]<()[]>)[[<>()][{}[]]
({{{{<([[((({{{}{}}<()[]>}{<()<>>{{}<>}})(<({}{})>({<>{}}[[]()]))){(<<<><>><()[]>>[{()()}{[]<>}
({<{[[{({{[<[{[][]}<[][]>]{(<><>)}>([[<>{}][<>{}]]({[]{}}<<>[]>))]}{[({[[]]{()[]}}{(<>{})[()()]})(<{(
[{<<<[(<(<{((([]{}))[{<>()}[()[]]]){{<{}{}>}[<[]<>>{<>{}}]}}<(<[<>[]][()()]>)<([{}()]{{}[]})
{{(([[([((<([[<><>]])>({[{()<>}<[]{}>]}<{[()()]<{}>}(<{}<>>({}{}))>))[{{([()()]<{}<>>){(<>{})(
([(<{[[{<{{<{([]())(<>[])}{{[]<>}{()<>}}>{{{()}}[<[]{}><{}<>>]}}<{[{()()}]{{<>[]}[<><>]}}<<{<>(
([[{[{[{<<(<{<{}{}>{[]}}{[{}{}]{()[]}}>[{({}[])}<[()[]]>])>>[(<<({<>{}}{[]{}})>>(<[([]()){()<>}]((()())([]
(({<({<([(({<<<>()>([]())>{<()[]>{[]<>}}}(<{{}<>}[()()]>({{}<>}[{}()]))))]){{<[{[(<>[]){()
([[(<{[[{<[<(<[]()>[{}[]]){[<><>]{<>[]}}>{{([]()){[]{}}}<((){})([]<>)>}]<<<{{}[]}[()]>(<{}><[][]>)>>>}
{{(<[{[([<<<[<{}<>>(<>{})]<({}[])[<>[]]>>({<{}{}><[]{}>}<<[]><(){}>>)>>(((({()()}[[]{}]))<[{[]<>)<[]()>]
(({{<<[{([[({[[]{}]{()<>}}[(<><>)[()()]])[<[<>[]]><([]{})[[][]]>]](<((<><>)<<>()>)[([][])((){})]>[(
((<<([[<{[{({<(){}><[][]>}{(()[])({}[])})({[{}()]({}{})}(<(){}>(<><>)))}{{[{()<>}<{}{}>][{[]{}}(()
<{(((([<[((({{{}<>}[[]<>]}<[{}<>]>)[<({}{})>{{[]()}<{}()>}])<([<<>>(<><>)]((()())(<>{})))>){(({(
<{{<<{{{[({{[<()[]>(()[])]}<<[[]<>][[]]>>}[<[({})<<>[]>][[[]]([][])]>])]}}(<({[[<[(){}]>{<[]{}>}]{(({
[([[(({([{{({{()}[{}<>]}{({}<>){{}()}}]}}{[<<({}())<(){}>>[{()[]}([]{})]>]{<<{{}()}(<>[])>{[(
[{[{[([<<((<<{()<>}<<>()>>[{[]{}}{{}[]}]>[[{[][]}{{}}]])(([((){})(()())]{[(){}]{()}})))}{(<<<<<><>>({}[]
<[{({[({[({{(<[]()>{{}<>}){{{}<>}[(){}]}}(([{}()]<[][]>)[[<>]({}{})])}<<[(<>)({})]<<()[]><
[((([<(({<<({{{}()}({}<>)}({()[]}[{}{}]))>{[{(<>[])}{(<>[])<{}[]>}]{<[<><>][()[]]>}}>({<{<<>()><<><>>}([{}[]]
{({((<<([((<[[()[]]{[][]}]<{(){}}{<>{}}>>({[(){}][<>]})))(<(({<>[]}<(){}>)(<()[]><{}()>))>)]){
<{<[<(<{<[({{{{}<>}<<>{}>}{[[]()][{}{}]}}[({<><>}{<>{}})[[{}()]{[]()}]])({{<[])(<>[])}})](<<[[<><>]](<{}{}>
[([[[{[((<<(<<()()>>)><<{([]()){<>{}}}<{[]{}}<()()>>>[(<<><>>[()[]]){((){})([]{})}]>>({[<[<><>]{<><
<{{({{{[<{[{{{()<>}[<><>]}[(()[]){[]{}}]}(<{{}[]}[<>[]]><{{}{}}<{}[]>>)]{(({(){}}<<>{}>)[<<><>>[{}
[[([[{[({[{[({{}[]}{()[]})[<()()>{{}{}}]][(([]<>)<[][]>)[<{}{}><{}()>]]}][<([([][]){()()}][[{}{}]{()<
{(<<(((<((((<{()<>}<<>[]>)[<[][]>[{}()]]){[[[]<>]<(){}>][<()<>>{{}<>}]})))<[{{[{{}{}}<[]<>>]}}(
{[(<{[<{{({[{[<><>](<>{})}{({}[])(<>{})}]}({<({}[])<[]<>>>(({}[]))}[<<()><<>>}[{()[]}{[][]}]])){[({<<>()>(
<([{[(<(<<([((()())<{}{}>)]<{(<>())(<>()]}{[()<>](<>())}>)<[[<[][]>]{{()}<<><>>}](({()()}[[
<[<[<{{{[{((<(()()){{}<>)><[[]()](()<>)>))({[[<>{}]{{}()}]({()<>}(()[]))})}]}([{((({{}()}[()<
[{([({[<(<{[{[<>[]][<>()]}([[]{}](()()))){{[()()]<(){}>}({()[]}<[]()>)}}<{[(<>[]){()<>}][[()<>]{()[]}]}{<(<>
{((<(<({{([{[([]<>){[]<>}](<[]<>>[[]<>])}{{<[][]><()[]>}({()<>}<<>{}>)}]<[<[<>()]([]{})><{{}<>}<{}<>>>][(
{<<([<(<{[[{{{<>[]}[[]<>]}{[{}[]]]}{<[(){}]>{[{}()]{[]<>}}}](<{[[]<>]{<>[]}}<<()<>>[[]()]>>)]<[{{<{}>[{}]}<(
[[{{{<{[{({<<<[]{}>[()<>]><[[]<>]([]<>)>><{<<>()>[<>{}]}>}((<[{}{}]{[]}]{<[]<>>{<>{}}})[([<>(
[[{<<{{[(([[[{()[]}][[()[]]<[]>]]({{{}}})][({([][])[{}{}]}<[(){}]<()[]>>){<{[]{}}[(){}]><{{}{}}<<>()>]}]))<<
[(({[<<{<({<([<><>])[{<>()>{{}[]}]>((<()<>><{}<>>)[{[][]}([]{})])})<{{([[]<>]<{}<>>)([()[]]{()()}
[([(({(<[<[<((<>{})[[]<>]){[<><>]({}[]>}>]>]>)}[(({(<<[{(){}}[()[]]]>[<(<>{}){{}{}}>[[()<>][()]]]>)
{<{{<({<{((<{({})<<>{}>}((()){()<>})>))}((<{((()[]){{}[]})[<<>>[[]<>]]}(([<>](()<>)))><{{{<>()}((){}}}((
<[<{<((({{[<{{[][]}}<([]<>)(<>{})>>]}[(([{()()}{<>()}])[<[()[]][()[]]>]){<<[<>()](<>{})>{{(){}}(<>
(([{([{[<(<(((()<>))[(())(<>{})])([[{}<>]{{}[]}][{<><>}[{}{}]])>[(([()[]]<[][]>)[{{}[]}(()[])])(([{}{}]
{<(<<{<[{<{<<<<>[]>[[]<>]){[[]()][<><>]}>({(<><>)(()<>)})}>[<([{{}{}}<[]<>>])({{[]<>}({}[])})>]}{<<[(
<{([({{{<{[{(([]())<<><>>)<[()()]((){})>}]}(<{(<(){}>(<>()))}([[()[]][(){}]](<<>{}>[{}()])}>)>([{<(
((([{<<[{{[(<<[]<>>(<>())>{({}{})<{}[]>})[[<()()>[<>[]]][<{}[]>(()())]]]}}]>>)]{{{{[[{[[[([]<>){
({(<{{({[[{<<(()[])[()]>[{<><>}{<>[]}]>{<{<><>}{()[]}>{[{}()]{[][]}}}}{<<{[]<>}(<><>)>{{[]{}}[
(<[{{(([<{{(<[<>()]((){})>{<{}[]>({}())})}}>][<[{{([{}[]])<([]<>)<<>{}>>}}{<({[][]}(()()))(<<>()>{
(<<{{{((<{({<<{}()><{}{}>><<()[]>[<>[]]>>(<[(){}]([]<>)>[({}<>)]))(({{[]<>}<()<>>}[<()[]>(()[])]){<[
<[(((<({([({{[[]()]{[]()}}([{}()]<[]<>>)}[[<()[]>{{}{}}]([<>]<<>()>)]){[((()<>){<>[]}){[{}[]){[
(({[[({{{[{{({(){}}{{}[]})<({}[])([]<>)>}[[(<>{})]<([]()){{}()}>]}[{<{[]<>}<()()>>([{}<>]<{
<[({{[<[{({[({[]<>}{{}[]})[{[][]}{[][]}]][[<{}[]>{[]()}]([()[]]({}<>))]}{<{[{}<>]<[]()>}<<[]()>[<>{}]>><((
[{[{<{{[<<[[<<{}<>>>][{{{}[]}({}())}]]([{<<><>>({}{})}{{[]<>}}]{{{[]()}([]<>)}})><({{<[][]>}}){<{{()><()>}>[<
{{({([<({(<[({{}{}}<[]{}>)]>[(((<>()){<>()]))[<({}[])(<>{})>{<<><>>{[]()}}]]){{[<(()[])<()<>>>(<()<>>)]([<{}
[({[<(<<[{<({<{}()>{{}()}})({({})<()()>}[{[]<>}[{}{}]})><[(({}{}))(((){})[[][]])]>}<{([<[]<>>]<[{}[]]((
[<{{{<<(<[[{<([][]){<>}>}{<[[]]{[]{}}><{<>{}}>}]<<{([]())[<>[]]}><(([]{}){[]<>})[(<>())({}<>}]>>]("""

FULL_SOL = []