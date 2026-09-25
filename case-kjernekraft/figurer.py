"""Figurer til notatet om nytten av kjernekraft. Lineær etterspørsel P = a - X."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

a = 140                 # etterspørsel: P = a - X
Qs, dQ, c = 80, 20, 25  # eksisterende produksjon Q*, kjernekraft ΔQ_N, enhetskostnad c
Q1 = Qs + dQ
P0, P1 = a - Qs, a - Q1 # autarkipriser: 60 og 40
D = lambda x: a - x
Xinv = lambda p: a - p

def grunnfigur(tittel):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot([0, a], [D(0), D(a)], 'k', lw=2); ax.text(122, 8, r'$D$', fontsize=13)
    ax.plot([Qs, Qs], [0, 135], color='tab:gray', lw=2); ax.text(Qs - 2, 130, r'$S_0$', ha='right', fontsize=12)
    ax.plot([Qs, Q1, Q1], [c, c, 135], color='tab:orange', lw=2); ax.text(Q1 + 2, 130, r'$S_1$', fontsize=12)
    ax.set_xlim(0, 145); ax.set_ylim(0, 140); ax.set_xticks([]); ax.set_yticks([])
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
    ax.text(145, -4, r'$X,\ Q$', ha='right', va='top', fontsize=12)
    ax.text(-3, 138, r'$P$', ha='right', va='top', fontsize=12)
    ax.set_title(tittel, fontsize=12)
    return fig, ax

def hlinje(ax, p, lab, **kw):
    ax.axhline(p, color=kw.get('color', 'gray'), ls=kw.get('ls', ':'), lw=kw.get('lw', 1))
    ax.text(-3, p, lab, ha='right', va='center', fontsize=12, color=kw.get('color', 'black'))

def vlinje(ax, q, top, lab):
    ax.plot([q, q], [0, top], color='gray', ls=':', lw=1)
    ax.text(q, -4, lab, ha='center', va='top', fontsize=12)

def pil(ax, x0, x1, y, lab):
    ax.annotate('', xy=(x0, y), xytext=(x1, y), arrowprops=dict(arrowstyle='<->'))
    ax.text((x0 + x1) / 2, y + 1.5, lab, ha='center', va='bottom', fontsize=11)

# ---------- Figur 1: lukket økonomi ----------
fig, ax = grunnfigur('Figur 1. Lukket økonomi')
hlinje(ax, P0, r'$P_0$'); hlinje(ax, P1, r'$P_1$'); hlinje(ax, c, r'$c$')
ax.add_patch(Rectangle((0, P1), Qs, P0 - P1, facecolor='tab:blue', alpha=0.15, hatch='//', edgecolor='tab:blue'))
ax.add_patch(Polygon([(Qs, P1), (Qs, P0), (Q1, P1)], color='tab:blue', alpha=0.6))
ax.add_patch(Rectangle((Qs, c), dQ, P1 - c, color='tab:green', alpha=0.5))
vlinje(ax, Qs, P0, r'$Q^*$'); vlinje(ax, Q1, P1, r'$Q_1$')
ax.text(Qs / 2, (P0 + P1) / 2, 'A: overføring fra produsenter\ntil konsumenter', ha='center', va='center', fontsize=10)
ax.annotate(r'B: $-\frac{1}{2}\Delta P\,\Delta Q_N$', xy=(Qs + 5, P1 + 5), xytext=(104, 88), fontsize=11, arrowprops=dict(arrowstyle='->'))
ax.annotate(r'C: $(P_1-c)\,\Delta Q_N$', xy=(Qs + dQ / 2, (P1 + c) / 2), xytext=(108, 55), fontsize=11, arrowprops=dict(arrowstyle='->'))
fig.tight_layout(); fig.savefig('figur1_lukket.png', dpi=200)

# ---------- Figur 2: verdensmarkedspris over autarkipris ----------
Pv = 70; Xv = Xinv(Pv)
fig, ax = grunnfigur(r'Figur 2. Åpen økonomi, $P_v > P_0$')
hlinje(ax, Pv, r'$P_v$', color='tab:red', ls='-', lw=1.5); hlinje(ax, P0, r'$P_0$'); hlinje(ax, c, r'$c$')
ax.add_patch(Rectangle((Qs, c), dQ, Pv - c, color='tab:green', alpha=0.5))
vlinje(ax, Xv, Pv, r'$X_v$'); vlinje(ax, Qs, Pv, r'$Q^*$'); vlinje(ax, Q1, Pv, r'$Q_1$')
pil(ax, Xv, Qs, Pv + 10, r'$E_0$'); pil(ax, Xv, Q1, Pv + 22, r'$E_1$')
ax.annotate(r'$(P_v-c)\,\Delta Q_N$', xy=(Qs + dQ / 2, (Pv + c) / 2), xytext=(108, 40), fontsize=11, arrowprops=dict(arrowstyle='->'))
fig.tight_layout(); fig.savefig('figur2_pv_over.png', dpi=200)

# ---------- Figur 3: P1 < P_v < P0 ----------
Pv = 50; Xv = Xinv(Pv)
fig, ax = grunnfigur(r'Figur 3. Åpen økonomi, $P_1 < P_v < P_0$')
hlinje(ax, P0, r'$P_0$'); hlinje(ax, Pv, r'$P_v$', color='tab:red', ls='-', lw=1.5); hlinje(ax, P1, r'$P_1$'); hlinje(ax, c, r'$c$')
ax.add_patch(Rectangle((Qs, c), Xv - Qs, Pv - c, color='tab:green', alpha=0.35))
ax.add_patch(Rectangle((Xv, c), Q1 - Xv, Pv - c, color='tab:green', alpha=0.6))
vlinje(ax, Qs, Pv, r'$Q^*$'); vlinje(ax, Xv, Pv, r'$X_v$'); vlinje(ax, Q1, Pv, r'$Q_1$')
pil(ax, Qs, Xv, Pv + 12, r'$M_0$'); pil(ax, Xv, Q1, Pv + 12, r'$E_1$')
ax.annotate('erstatter import', xy=(Qs + 5, 33), xytext=(20, 15), fontsize=10, arrowprops=dict(arrowstyle='->'))
ax.annotate('ny eksport', xy=(Q1 - 5, 33), xytext=(112, 48), fontsize=10, arrowprops=dict(arrowstyle='->'))
fig.tight_layout(); fig.savefig('figur3_pv_mellom.png', dpi=200)
