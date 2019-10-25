# 1、常用命令
**查看MySQL提供的所有存储引擎**
```
mysql> show engines;
```
<img src="https://img2018.cnblogs.com/blog/1825659/201910/1825659-20191018201547750-1820716923..png" alt="查看存储引擎" />
从上图我们可以查看出 MySQL 当前默认的存储引擎是InnoDB,并且在5.7版本所有的存储引擎中只有 InnoDB 是事务性存储引擎，也就是说只有 InnoDB 支持事务。
**查看MySQL当前默认的存储引擎**
我们也可以通过下面的命令查看默认的存储引擎。
```
mysql> show variables like '%storage_engine%';
```
**查看表的存储引擎**
```
show table status like "table_name" ;
```
<img src="https://img2018.cnblogs.com/blog/1825659/201910/1825659-20191018201548334-1111264954..png" alt="查看表存储引擎" />
# 2、MyISAM和InnoDB区别
​ MyISAM是MySQL的默认数据库引擎（5.5版之前）。虽然性能极佳，而且提供了大量的特性，包括全文索引、压缩、空间函数等，但MyISAM不支持事务和行级锁，而且最大的缺陷就是崩溃后无法安全恢复。不过，5.5版本之后，MySQL引入了InnoDB（事务性数据库引擎），MySQL 5.5版本后默认的存储引擎为InnoDB。
​ 大多数时候我们使用的都是 InnoDB 存储引擎，但是在某些情况下使用 MyISAM 也是合适的比如读密集的情况下。（如果你不介意 MyISAM 崩溃回复问题的话）。
**两者的对比：**
<ol>
- **是否支持行级锁** : MyISAM 只有表级锁(table-level locking)，而InnoDB 支持行级锁(row-level locking)和表级锁,默认为行级锁。
- **是否支持事务和崩溃后的安全恢复：MyISAM** 强调的是性能，每次查询具有原子性,其执行比InnoDB类型更快，但是不提供事务支持。但是**InnoDB** 提供事务支持事务，外部键等高级数据库功能。具有事务(commit)、回滚(rollback)和崩溃修复能力(crash recovery capabilities)的事务安全(transaction-safe (ACID compliant))型表。
- **是否支持外键：** MyISAM不支持，而InnoDB支持。
- **是否支持MVCC** ：仅 InnoDB 支持。应对高并发事务, MVCC比单纯的加锁更高效;MVCC只在 `READ COMMITTED` 和 `REPEATABLE READ` 两个隔离级别下工作;MVCC可以使用 乐观(optimistic)锁 和 悲观(pessimistic)锁来实现;各数据库中MVCC实现并不统一。
- ......
</ol>
《MySQL高性能》上面有一句话这样写到:
<blockquote>
不要轻易相信“MyISAM比InnoDB快”之类的经验之谈，这个结论往往不是绝对的。在很多我们已知场景中，InnoDB的速度都可以让MyISAM望尘莫及，尤其是用到了聚簇索引，或者需要访问的数据都可以放入内存的应用。
</blockquote>
​ 一般情况下我们选择 InnoDB 都是没有问题的，但是某事情况下你并不在乎可扩展能力和并发能力，也不需要事务支持，也不在乎崩溃后的安全恢复问题的话，选择MyISAM也是一个不错的选择。但是一般情况下，我们都是需要考虑到这些问题的。